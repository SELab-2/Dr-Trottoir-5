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
     * @param args
     */
    fetch(context: any, args: {needsLogin}) {
      if (context.state.currentUser === null) {
        const style = args && args.needsLogin && args.needsLogin === true ? "SNACKBAR" : "NONE";
        context.commit("SET_CURRENTUSER", RequestHandler.handle(UserService.get(), {
          id: "getUserError",
          style: style
        }).catch(() => {}));
      }
    },

    /**
     * Clear the currently stored user
     * @param context
     */
    clear(context: any) {
      if (context.state.currentUser !== null) context.state.currentUser = null;
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
      return state.currentUser.then(() => true).catch(() => false);
    },

    /**
     * Get if the client is admin (logged in).
     *
     * @param state
     */
    isAdmin(state: any): Promise<boolean> {
      return state.currentUser
      .then(u => u.role === UserRole.AD || u.role === UserRole.SU)
      .catch(() => false);
    },
  },
};
