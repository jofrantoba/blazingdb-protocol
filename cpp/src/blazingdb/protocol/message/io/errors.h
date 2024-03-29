#ifndef BLAZINGDB_PROTOCOL_IO_ERRORS_H_
#define BLAZINGDB_PROTOCOL_IO_ERRORS_H_

#include <blazingdb/protocol/message/errors.h>

namespace blazingdb {
namespace protocol {
namespace io {
namespace errors {

using protocol::errors::Error;

//! Thrown by io calls when the query-string is invalid.

class IOError : public Error {
    
};

}  // namespace errors
}  // namespace io
}  // namespace message
}  // namespace blazingdb

#endif
