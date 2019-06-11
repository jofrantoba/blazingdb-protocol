#ifndef _BLAZINGDB_PROTOCOL_API_H_
#define _BLAZINGDB_PROTOCOL_API_H_

#include "buffer/buffer.h"
#include "client/client.h"
#include "connection/unix_socket_connection.h"
#include "connection/tcp_connection.h"
#include "server/server.h"
#include "message/messages.h"

namespace blazingdb {
namespace protocol {

// TODO(gcca): serializable through output stream
template <class Frame>
class Protocol {
public:
  //// TODO(gcca): reading input stream
  const Frame &frameFrom(const Buffer &buffer) const {
    const auto *frame = reinterpret_cast<const Frame *>(buffer.data());
    return *frame;
  }

  const Buffer payloadFrom(const Buffer &buffer) const {
    return buffer.slice(static_cast<std::ptrdiff_t>(sizeof(Frame)));
  }
};

}  // namespace protocol
}  // namespace blazingdb

#endif
