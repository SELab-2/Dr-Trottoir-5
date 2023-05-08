import { EchoError, EchoPromise } from 'echofetch'
import { CustomErrorOptions } from './error/types/CustomErrorOptions'
import { ErrorHandler } from './error/ErrorHandler'

export class RequestHandler {
    /**
     * Handle a request.
     * @param request
     * @param errorOptions
     */
    static handle<T> (
        request: EchoPromise<T>,
        errorOptions: CustomErrorOptions
    ): EchoPromise<T> {
        // Handle the error when it occurs.
        request.getPromise().catch(async (error: EchoError) => {
          await ErrorHandler.handle(error, errorOptions)
        })

        return request
    }
}
