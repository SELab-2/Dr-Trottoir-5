import {EchoPromise} from "echofetch";
import User from "@/api/models/User";
import UserService from "@/api/services/UserService";
import {UserRole} from "@/api/models/UserRole";
import {RequestHandler} from "@/api/RequestHandler";

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
    SET_CURRENTUSER(state: any, currentUser: User) {
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
        RequestHandler.handle(UserService.get(), {
          id: "getUserError",
          style: "SNACKBAR"
        }).then(user => {
          context.commit("SET_CURRENTUSER", user);
        });
      }
    },
  },

  getters: {
    /**
     * Get the current user.
     *
     * @param state
     */
    currentUser(state: any): User {
      return state.currentUser;
    },

    /**
     * Get if the client is authenticated (logged in).
     *
     * @param state
     */
    isAuthenticated(state: any): boolean {
      return !state.currentUser;
    },

    /**
     * Get if the client is admin (logged in).
     *
     * @param state
     */
    isAdmin(state: any): boolean {
      return (
        state.currentUser &&
        (
          state.currentUser.role == UserRole.AD ||
          state.currentUser.role == UserRole.SU
        )
      );
    },
  },
};
