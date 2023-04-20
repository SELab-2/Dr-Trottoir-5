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
    ST: [
      'student_home', 'dagplanning', 'account', 'unauthorized', 'home', 'student_post_edit', 'student_post',
      'student_post_view', 'building_info', 'building_student'
    ],
    SY: ['syndicus_home', 'account', 'unauthorized', 'home'],
    SU: [
      'admin_home', 'dagplanning', 'account', 'unauthorized', 'home', 'create_building', 'create_location', 'create_round',
      'studenttemplate', 'users', 'studenttemplates', 'add_studenttemplate', 'ronde_dagplanningen', 'dagplanning_edit', 'dagplanning_add',
      'create_mail-template', 'buildings', 'rounds', 'students', 'syndicusen', 'mailtemplates'
    ],
    AD: [
      'admin_home', 'account', 'unauthorized', 'home', 'create_building', 'create_location', 'create_round',
      'studenttemplate', 'users', 'studenttemplates', 'add_studenttemplate', 'ronde_dagplanningen', 'dagplanning_edit', 'dagplanning_add',
       'create_mail-template', 'buildings', 'rounds', 'students', 'syndicusen', 'mailtemplates'
    ]
  }
};
