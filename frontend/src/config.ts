export default {
  FRONTEND: {
    URL: (<string>process.env.VUE_APP_FRONTEND_URL).endsWith('/') ? (<string>process.env.VUE_APP_FRONTEND_URL).substring(0, (<string>process.env.VUE_APP_FRONTEND_URL).length - 1) : (<string>process.env.VUE_APP_FRONTEND_URL),
  },

  BACKEND: {
    URL: (<string>process.env.VUE_APP_BACKEND_URL).endsWith('/') ? (<string>process.env.VUE_APP_BACKEND_URL).substring(0, (<string>process.env.VUE_APP_BACKEND_URL).length - 1) : (<string>process.env.VUE_APP_BACKEND_URL),
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
      'create_mail-template', 'buildings', 'rounds', 'students', 'syndici', 'mailtemplates', 'trashtemplates', 'editTrashtemplates',
      'createTrashtemplates', 'trashtemplateContainers', 'createTrashtemplateContainers', 'editTrashtemplateContainers',
      'trashtemplateBuildings', 'editTrashtemplateBuildings', 'mail-template-edit', 'edit_round',
      'admin_info_user', 'admin_edit_user', 'admin_user_register', 'editTrashtemplateBuilding', 'addBuildingsToTrashTemplate', 'send_mail',
      'student_home', 'dagplanning', 'student_post_edit', 'student_post', 'student_post_view', 'building_info', 'building_student'
    ],
    AD: [
      'admin_home', 'account', 'unauthorized', 'home', 'create_building', 'create_location', 'create_round',
      'studenttemplate', 'users', 'studenttemplates', 'add_studenttemplate', 'ronde_dagplanningen', 'dagplanning_edit', 'dagplanning_add',
      'create_mail-template', 'buildings', 'rounds', 'students', 'syndici', 'mailtemplates', 'trashtemplates', 'editTrashtemplates',
      'createTrashtemplates', 'trashtemplateContainers', 'createTrashtemplateContainers', 'editTrashtemplateContainers',
      'trashtemplateBuildings', 'editTrashtemplateBuildings', 'mail-template-edit', 'admin_info_building',
      'admin_edit_building', 'admin_info_user', 'admin_edit_user', 'admin_user_register', 'syndicus_create', 'syndicus_adjust', 'locations',
      'edit_round', 'adminRoundView', 'editTrashtemplateBuilding', 'addBuildingsToTrashTemplate', 'send_mail',
      'student_home', 'dagplanning', 'student_post_edit', 'student_post', 'student_post_view', 'building_info', 'building_student'
    ]
  }
};
