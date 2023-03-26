import {
  Body,
  DELETE,
  EchoPromise,
  EchoService,
  EchoServiceBuilder,
  GET,
  PATCH,
  POST
} from "../EchoFetch/src/echofetch";
import User from "../models/User";
import config from "@/config";
import { AuthInterceptor } from "@/api/interceptors/AuthInterceptor";
import { InputFields } from "@/types/fields/InputFields";

class UserService extends EchoService {
    /**
     * Get the logged in user.
     */
    @GET("/user")
    get(): EchoPromise<User> {
        return {} as EchoPromise<User>;
    }

  /**
   * Login a user based on
   */
  @POST("/user/login")
  login(): EchoPromise<User> {
    return {} as EchoPromise<User>;
  }

    /**
     * Update the current user
     */
    @PATCH("/user")
    update(@Body() body: InputFields): EchoPromise<string> {
        return {} as EchoPromise<string>;
    }


    /**
     * Delete the logged in user.
     */
    @DELETE("/user")
    delete(): EchoPromise<void> {
        return {} as EchoPromise<void>;
    }

}

export default new EchoServiceBuilder()
    .setBaseUrl(config.BACKEND.URL)
    .addInterceptor(new AuthInterceptor())
    .build(UserService);
