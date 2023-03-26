import {
  EchoError,
  EchoRequest,
  EchoResponse,
  EchoServiceInterceptor,
} from "../EchoFetch/src/echofetch";
import {setupCache} from 'axios-cache-adapter';

/**
 * Setup the cache.
 * This is still needed for browsers that do not support serviceworkers
 *
 */
function setupCacheStore() {
  return setupCache({
    maxAge: 15 * 60 * 1000,
  });
}

// Create a cache for storing the network results.
let cache = setupCacheStore();

export class AuthInterceptor implements EchoServiceInterceptor {
  onRequest(request: EchoRequest): EchoRequest {
    // Send credentials with every request.
    request.withCredentials = true;

    // Clear the cache when logging out.
    // Clear the cache when deleting data.
    // Clear the cache when posting data.
    // Clear the cache when patching data.
    if (
      request.url?.includes("logout") || // Making sure that if a person logs out their data is also gone
      request.method?.toLowerCase() === "DELETE" || // Making sure that if a person deletes it's also gone from the cache
      request.method?.toLowerCase() === "POST" || // Making sure that if a person makes a new object it also gets pulled from the api afterwards
      request.method?.toLowerCase() === "PATCH" // Making sure that if a person updates a new object it gets refreshed
    ) {
      cache = setupCacheStore();
    }

    // Cache every request.
    request.adapter = cache.adapter;

    return request;
  }

  onResponse(response: EchoResponse): EchoResponse {
    return response;
  }

  onError(error: EchoError): EchoError {
    return error;
  }
}
