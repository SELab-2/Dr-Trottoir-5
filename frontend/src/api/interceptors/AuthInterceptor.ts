import {
  EchoError,
  EchoRequest,
  EchoResponse,
  EchoServiceInterceptor,
} from 'echofetch';
import router from '@/router'

// Create a cache for storing the network results.

export class AuthInterceptor implements EchoServiceInterceptor {

  onRequest(request: EchoRequest): EchoRequest {
    return request;
  }

  onResponse(response: EchoResponse): EchoResponse {
    return response;
  }

  onError(error: EchoError): EchoError {
    return error;
  }
}
