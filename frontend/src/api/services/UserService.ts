import {Body, DELETE, EchoPromise, EchoService, EchoServiceBuilder, GET, PATCH, Path, POST} from "echofetch";
import User from "../models/User";
import config from "@/config";
import {AuthInterceptor} from "@/api/interceptors/AuthInterceptor";
import {InputFields} from "@/types/fields/InputFields";
import {AuthLoginWrapper} from "@/api/wrappers/AuthWrappers";
import {UserRole} from "@/api/models/UserRole";

class UserService extends EchoService {
  /**
   * Get the logged in user.
   */
  @GET("/user/")
  get(): EchoPromise<User> {
    return {} as EchoPromise<User>;
  }

  /**
   * Get user by id
   */
  @GET("/user/{id}/")
  getUserById(@Path('id') id: number): EchoPromise<User> {
    return {} as EchoPromise<User>
  }

  /**
   * Patch user by id
   */
  @PATCH("/user/{id}/")
  updateUserById(@Path('id') id: number, @Body() body: {}): EchoPromise<User> {
    return {} as EchoPromise<User>
  }

  /**
   * Delete user by id
   */
  @DELETE("/user/{id}/")
  deleteUserById(@Path('id') id: number): EchoPromise<void> {
    return {} as EchoPromise<void>
  }


  /**
   * Get the logged in user.
   * Get all users.
   */
  @GET("/users/")
  getUsers(): EchoPromise<User[]> {
    return {} as EchoPromise<User[]>;
  }

  /**
   * Login a user based on
   */
  @POST("/login/")
  login(@Body() body: AuthLoginWrapper): EchoPromise<User> {
    return {} as EchoPromise<User>;
  }

  /**
   * Get the role of the logged in user.
   */
  @GET("/role/")
  getRole(): EchoPromise<UserRole> {
    return {} as EchoPromise<UserRole>;
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
