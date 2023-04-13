export default {
  FRONTEND: {
    URL: process.env.VUE_APP_FRONTEND_URL,
  },

  BACKEND: {
    URL: process.env.VUE_APP_BACKEND_URL,
  },

  /**
   * A list of allowed pages per rank
   */
  AUTHORIZED: {
    AA: ['register_done', 'account', 'unauthorized', 'home'],
    BE: ['resident_home', 'account', 'unauthorized', 'home'],
    ST: ['student_home', 'dagplanning', 'account', 'unauthorized', 'home'],
    SY: ['syndicus_home', 'account', 'unauthorized', 'home'],
    SU: ['admin_home', 'dagplanning', 'account', 'unauthorized', 'home'],
    AD: ['admin_home', 'account', 'unauthorized', 'home']
  }
};
