#include <blazingdb/protocol/message/interpreter/utils.h>

#include <string>
#include <functional>
#include <typeinfo>

#include <blazingdb/protocol/api.h>
#include <iostream>
#include "flatbuffers/flatbuffers.h"
#include <blazingdb/protocol/message/interpreter/gdf_dto.h>

namespace blazingdb {
namespace protocol {

flatbuffers::Offset<flatbuffers::Vector<int8_t>> BuildCudaIpcMemHandler (flatbuffers::FlatBufferBuilder &builder, const std::basic_string<int8_t> &reserved) {
  return builder.CreateVector(reserved.data(), reserved.size());
}

std::basic_string<int8_t> CudaIpcMemHandlerFrom (const gdf::cudaIpcMemHandle_t *handler) {
  auto vector_bytes = handler->reserved();
  return std::basic_string<int8_t>{vector_bytes->data(), vector_bytes->size()};
}

flatbuffers::Offset<flatbuffers::Vector<int8_t>> BuildDirectCudaIpcMemHandler (flatbuffers::FlatBufferBuilder &builder, const flatbuffers::Vector<int8_t> * data) {
  return builder.CreateVector(data->data(), data->size());
}

flatbuffers::Offset<flatbuffers::Vector<int8_t>> BuildCustringsData (flatbuffers::FlatBufferBuilder &builder, const std::basic_string<int8_t> &reserved) {
  return builder.CreateVector(reserved.data(), reserved.size());
}

std::basic_string<int8_t> CustringsDataFrom (const gdf::custringsData_t *handler) {
  auto vector_bytes = handler->reserved();
  return std::basic_string<int8_t>{vector_bytes->data(), vector_bytes->size()};
}

std::vector<::gdf_dto::gdf_column>  GdfColumnsFrom(const flatbuffers::Vector<flatbuffers::Offset<blazingdb::protocol::gdf::gdf_column_handler>> *rawColumns) {
  std::vector<::gdf_dto::gdf_column>  columns;
  for (const auto& c : *rawColumns){
    bool valid_valid = (c->valid()->reserved()->size() == 64);
    ::gdf_dto::gdf_column column = {
        .data = CudaIpcMemHandlerFrom(c->data()),
        .valid = valid_valid ? CudaIpcMemHandlerFrom(c->valid()) : std::basic_string<int8_t>{},
        .size = c->size(),
        .dtype = (gdf_dto::gdf_dtype)c->dtype(),
        .null_count = c->null_count(),
        .dtype_info = gdf_dto::gdf_dtype_extra_info {
            .time_unit = (gdf_dto::gdf_time_unit) c->dtype_info()->time_unit(),
        },
        .custrings_data = CustringsDataFrom(c->custrings_data())
    };
    columns.push_back(column);
  }
  return columns;
}

std::vector<std::string> ColumnNamesFrom(const flatbuffers::Vector<flatbuffers::Offset<flatbuffers::String>> *rawNames) {
  std::vector<std::string> columnNames;
  for (const auto& rawName : *rawNames){
    auto name = std::string{rawName->c_str()};  
    columnNames.push_back(name);
  }
  return columnNames;
}

std::vector<uint64_t> ColumnTokensFrom(const flatbuffers::Vector<uint64_t> *rawColumnTokens) {
  std::vector<uint64_t> columnTokens;
  for (const auto& rawColumnToken : *rawColumnTokens){
    auto columnToken = rawColumnToken;
    columnTokens.push_back(columnToken);
  }
  return columnTokens;
}

std::vector<flatbuffers::Offset<gdf::gdf_column_handler>>  BuildFlatColumns(flatbuffers::FlatBufferBuilder &builder, const std::vector<::gdf_dto::gdf_column> &columns) {
  std::vector<flatbuffers::Offset<gdf::gdf_column_handler>> offsets;
  for (auto & c: columns) {
    auto dtype_extra_info = gdf::Creategdf_dtype_extra_info (builder, (gdf::gdf_time_unit)c.dtype_info.time_unit );
    auto data_offset = gdf::CreatecudaIpcMemHandle_t(builder, BuildCudaIpcMemHandler (builder, c.data) );
    auto valid_offset = gdf::CreatecudaIpcMemHandle_t(builder, BuildCudaIpcMemHandler(builder, c.valid) );
    auto custrings_data_offset = gdf::CreatecustringsData_t(builder, BuildCustringsData(builder, c.custrings_data) );
    auto column_offset = ::blazingdb::protocol::gdf::Creategdf_column_handler(builder, data_offset, valid_offset, c.size, (gdf::gdf_dtype)c.dtype, dtype_extra_info, c.null_count, custrings_data_offset );
    offsets.push_back(column_offset);
  }
  return offsets;
};

std::vector<flatbuffers::Offset<flatbuffers::String>>  BuildFlatColumnNames(flatbuffers::FlatBufferBuilder &builder, const std::vector<std::string> &columnNames) {
  std::vector<flatbuffers::Offset<flatbuffers::String>> offsets;
  for (auto & name: columnNames) {
    offsets.push_back( builder.CreateString(name.data()));
  }
  return offsets;
};

flatbuffers::Offset<flatbuffers::Vector<uint64_t>>  BuildFlatColumnTokens(flatbuffers::FlatBufferBuilder &builder, const std::vector<uint64_t> &columnTokens) {
  return builder.CreateVector(columnTokens.data(), columnTokens.size());
}

flatbuffers::Offset<TableGroup> BuildTableGroup(flatbuffers::FlatBufferBuilder &builder,
                                                       const TableGroupDTO &tableGroup) {
  auto tableNameOffset = builder.CreateString(tableGroup.name);
  std::vector<flatbuffers::Offset<BlazingTable>> tablesOffset;

  for (auto table : tableGroup.tables) {
    auto columns = BuildFlatColumns(builder, table.columns);
    auto token_offsets = BuildFlatColumnTokens(builder, table.columnTokens);
    tablesOffset.push_back( CreateBlazingTable(builder, builder.CreateVector(columns), token_offsets, table.resultToken));
  }

  auto tables = builder.CreateVector(tablesOffset);
  return CreateTableGroup(builder, tables, tableNameOffset);
}


  flatbuffers::Offset<blazingdb::protocol::BlazingTable> BlazingTableSchema::Serialize(flatbuffers::FlatBufferBuilder &builder, const BlazingTableSchema &data) {
    auto columnsOffset = BuildFlatColumns(builder, data.columns);
    auto columnTokensOffset = BuildFlatColumnTokens(builder, data.columnTokens);
    return blazingdb::protocol::CreateBlazingTable(builder, builder.CreateVector(columnsOffset), columnTokensOffset, data.resultToken);
  }

  void BlazingTableSchema::Deserialize (const blazingdb::protocol::BlazingTable *pointer, BlazingTableSchema* schema){
      schema->columns = GdfColumnsFrom(pointer->columns());
      
      schema->columnTokens.clear();
      auto tokens_list = pointer->columnTokens();
      for (const auto &item : (*tokens_list)) {
        schema->columnTokens.push_back(item);
      }

      schema->resultToken = pointer->resultToken();
  }



  flatbuffers::Offset<blazingdb::protocol::TableSchema> TableSchemaSTL::Serialize(flatbuffers::FlatBufferBuilder &builder, const TableSchemaSTL &data) {
    auto namesOffset = builder.CreateVectorOfStrings(data.names);
    auto calciteToFileIndicesOffset = builder.CreateVector(data.calciteToFileIndices);
    auto typesOffset = builder.CreateVector(data.types);
    auto numRowGroupsOffset = builder.CreateVector(data.numRowGroups);
    auto filesOffset = builder.CreateVectorOfStrings(data.files);
    auto csvDelimiterOffset = builder.CreateString(data.csvDelimiter);
    auto csvLineTerminatorOffset = builder.CreateString(data.csvLineTerminator);

    return blazingdb::protocol::CreateTableSchema(builder, namesOffset, calciteToFileIndicesOffset, typesOffset, numRowGroupsOffset, filesOffset, csvDelimiterOffset, csvLineTerminatorOffset, data.csvSkipRows);
  }
  void TableSchemaSTL::Deserialize (const blazingdb::protocol::TableSchema *pointer, TableSchemaSTL* schema){
      schema->names.clear();
      auto names_list = pointer->names();
      for (const auto &item : (*names_list)) {
        schema->names.push_back(std::string{item->c_str()});
      }

      schema->calciteToFileIndices.clear();
      auto calciteToFileIndices_list = pointer->calciteToFileIndices();
      for (const auto &item : (*calciteToFileIndices_list)) {
        schema->calciteToFileIndices.push_back(item);
      }

      schema->types.clear();
      auto types_list = pointer->types();
      for (const auto &item : (*types_list)) {
        schema->types.push_back(item);
      }

      schema->numRowGroups.clear();
      auto numRowGroups_list = pointer->numRowGroups();
      for (const auto &item : (*numRowGroups_list)) {
        schema->numRowGroups.push_back(item);
      }

      schema->files.clear();
      auto files_list = pointer->files();
      for (const auto &item : (*files_list)) {
        schema->files.push_back(std::string{item->c_str()});
      }

      schema->csvDelimiter = std::string{pointer->csvDelimiter()->c_str()};

      schema->csvLineTerminator = std::string{pointer->csvLineTerminator()->c_str()};

      schema->csvSkipRows = pointer->csvSkipRows();
  }


}
}
