
#include <iostream>

#include <blazingdb/protocol/api.h>

#include <blazingdb/protocol/interpreter/messages.h>

namespace blazingdb {
  namespace protocol {

    namespace interpreter {

      auto InterpreterService(const blazingdb::protocol::Buffer &requestBuffer) -> blazingdb::protocol::Buffer {
        RequestMessage request{requestBuffer.data()};
        DMLRequestMessage requestPayload(request.getPayloadBuffer());

        std::cout << "header: " << request.messageType() << std::endl;
        std::cout << "query: " << requestPayload.getLogicalPlan() << std::endl;

        uint64_t token = 543210L;

        DMLResponseMessage responsePayload{token};
        ResponseMessage responseObject{Status_Success, responsePayload};
        auto bufferedData = responseObject.getBufferData();
        Buffer buffer{bufferedData->data(),
                      bufferedData->size()};
        return buffer;
      }

    }
  }
}

using namespace blazingdb::protocol::interpreter;

int main() {
  blazingdb::protocol::UnixSocketConnection connection({"/tmp/ral.socket", std::allocator<char>()});
  blazingdb::protocol::Server server(connection);


  server.handle(InterpreterService);

  return 0;
}
