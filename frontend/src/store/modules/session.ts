import User from "@/api/models/User";
import UserService from "@/api/services/UserService";
import {UserRole} from "@/api/models/UserRole";
import {RequestHandler} from "@/api/RequestHandler";
import {EchoPromise} from "@/api/EchoFetch";

export const session = {
  namespaced: true,

  state: {
    currentUser: null,
  },

  mutations: {
    /**
     * Set the logged in user.
     *
     * @param state
     * @param currentUser User that is logged in.
     */
    SET_CURRENTUSER(state: any, currentUser: EchoPromise<User>) {
      state.currentUser = currentUser;
    },
  },

  actions: {
    /**
     * Open a new modal.
     *
     * @param context
     */
    fetch(context: any) {
      if (!context.getters.currentUser) {
        context.commit("SET_CURRENTUSER", RequestHandler.handle(UserService.get(), {
          id: "getUserError",
          style: "SNACKBAR"
        }).catch(() => {}));
      }
    }
  },

  getters: {
    /**
     * Get the current user.
     *
     * @param state
     */
    currentUser(state: any): EchoPromise<User> {
      return state.currentUser;
    },

    /**
     * Get if the client is authenticated (logged in).
     *
     * @param state
     */
    isAuthenticated(state: any): boolean {
      return state.currentUser && state.currentUser.isSuccess();
    },

    /**
     * Get if the client is admin (logged in).
     *
     * @param state
     */
    isAdmin(state: any): boolean {
      return (
        state.currentUser && state.currentUser.isSuccess() &&
        (
          state.currentUser.requireData().role == UserRole.AD ||
          state.currentUser.requireData().role == UserRole.SU
        )
      );
    },
  },
};
