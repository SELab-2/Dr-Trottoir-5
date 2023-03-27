import {Body, DELETE, EchoPromise, EchoService, EchoServiceBuilder, GET, PATCH, POST} from "echofetch";
import User from "../models/User";
import config from "@/config";
import {AuthInterceptor} from "@/api/interceptors/AuthInterceptor";
import {InputFields} from "@/types/fields/InputFields";
import {AuthLoginWrapper, AuthRegisterWrapper} from "@/api/wrappers/AuthWrappers";

class UserService extends EchoService {
  /**
   * Get the logged in user.
   */
  @GET("/user/")
  get(): EchoPromise<User> {
    return {} as EchoPromise<User>;
  }

  /**
   * Login a user based on
   */
  @POST("/login/")
  login(@Body() body: AuthLoginWrapper): EchoPromise<User> {
    return {} as EchoPromise<User>;
  }

  /**
   * Update the current user
   * TODO Backend support
   */
  @PATCH("/user/")
  update(@Body() body: InputFields): EchoPromise<string> {
    return {} as EchoPromise<string>;
  }


  /**
   * Delete the logged in user.
   */
  @DELETE("/user/")
  delete(): EchoPromise<void> {
    return {} as EchoPromise<void>;
  }

}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .addInterceptor(new AuthInterceptor())
  .build(UserService);
