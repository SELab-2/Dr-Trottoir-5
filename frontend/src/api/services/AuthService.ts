import {
  Body,
  EchoPromise,
  EchoService,
  EchoServiceBuilder,
  POST,
} from 'echofetch';
import { ErrorHandler } from "@/api/error/ErrorHandler";
import { AuthInterceptor } from "@/api/interceptors/AuthInterceptor";
import config from "@/config";
import { store } from '../../store';
import router from "../../router";
import {AuthLoginWrapper, AuthRegisterWrapper} from "@/api/wrappers/AuthWrappers";
import User from "@/api/models/User";

class AuthService extends EchoService {
  /**
   * Login into an account.
   * @param body User parameters to login.
   */
  @POST("/login/")
  login(@Body() body: AuthRegisterWrapper): EchoPromise<User> {
    return {} as EchoPromise<User>;
  }

  /**
   * Create a new user.
   * @param body User parameters for the new user.
   */
  @POST("/register/")
  register(@Body() body: AuthLoginWrapper): EchoPromise<User> {
    return {} as EchoPromise<User>;
  }

  /**
   * Logout the current user.
   */
  @POST("/logout")
  logout(): EchoPromise<string> {
    return {} as EchoPromise<string>;
  }

  /**
   * Call the logout function and show the progress
   * @param goHome If the user should be send to the homepage after logging out.
   */
  handleLogout(goHome = false) {
    // Send loading message.
    store.dispatch("snackbar/open", {
      message: "Logging out...",
      color: "info",
      timeout: 120 * 1000,
    });

    this.logout()
      .then((_) => {
        // Send confirmation message.
        store.dispatch("snackbar/open", {
          message: "Successfully logged out",
          color: "success",
        });

        if (goHome) {
          router.push("/");
        }

        // Update the current user inside the store.
        store.dispatch("session/fetch");
      })
      .catch((error) => {
        ErrorHandler.handle(error, {
          style: "SECTION",
          id: "logout",
          displayFullpage: true,
        });
      });
  }
}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .addInterceptor(new AuthInterceptor())
  .build(AuthService);
