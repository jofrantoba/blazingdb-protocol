#ifndef BLAZINGDB_PROTOCOL_BUFFER_BUFFER_H_
#define BLAZINGDB_PROTOCOL_BUFFER_BUFFER_H_

#include <cstdint>
#include <string>
#include "flatbuffers/flatbuffers.h"

namespace blazingdb {
namespace protocol {

class Buffer : public std::basic_string<std::uint8_t> {
public:
  Buffer()
      : std::basic_string<std::uint8_t >() {}

  Buffer(const std::uint8_t *const data, const size_t size)
      : std::basic_string<std::uint8_t >(data, size) {}

  Buffer(const std::shared_ptr<flatbuffers::DetachedBuffer> & buffer)
      : std::basic_string<std::uint8_t >(buffer->data(), buffer->size()) {}

  Buffer slice(const std::ptrdiff_t offset) const {
    return {this->data() +  offset, this->size() - static_cast<std::size_t>(offset)};
  }
};

}  // namespace protocol
}  // namespace blazingdb

#endif
