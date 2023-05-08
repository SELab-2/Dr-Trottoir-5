import { Body, DELETE, EchoPromise, EchoService, EchoServiceBuilder, GET, PATCH, Path, POST } from '@/api/EchoFetch'
import StudentTemplate from '@/api/models/StudentTemplate'
import config from '@/config'
import { AuthInterceptor } from '@/api/interceptors/AuthInterceptor'
import DayPlanning from '@/api/models/Planning'

class StudentTemplateService extends EchoService {
  @GET('/studenttemplates/')
  getStudentTemplates (): EchoPromise<StudentTemplate[]> {
    return {} as EchoPromise<StudentTemplate[]>
  }

  @POST('/studenttemplates/')
  addStudentTemplate (@Body() body: {}): EchoPromise<any> {
    return {} as EchoPromise<any>
  }

  @PATCH('/studenttemplates/{id}/')
  updateStudentTemplate (@Path('id') id: number, @Body() body: {}): EchoPromise<any> {
    return {} as EchoPromise<any>
  }

  @DELETE('/studenttemplates/{id}/')
  deleteStudentTemplate (@Path('id') id: number): EchoPromise<any> {
    return {} as EchoPromise<any>
  }

  @GET('/studenttemplates/{template_id}/')
  getStudentTemplate (@Path('template_id') template_id: number): EchoPromise<StudentTemplate> {
    return {} as EchoPromise<StudentTemplate>
  }

  @POST('/studenttemplates/{template_id}/rondes/')
  addRound (@Path('template_id') template_id: number, @Body() body: {}): EchoPromise<any> {
    return {} as EchoPromise<any>
  }

  @DELETE('/studenttemplates/{template_id}/rondes/{ronde_id}/')
  removeRound (@Path('template_id') template_id: number,
              @Path('ronde_id') ronde_id: number): EchoPromise<any> {
    return {} as EchoPromise<any>
  }

  @GET('/studenttemplates/{template_id}/rondes/{ronde_id}/dagplanningen/')
  getDagPlanningen (@Path('template_id') template_id: number,
              @Path('ronde_id') ronde_id: number): EchoPromise<DayPlanning[]> {
    return {} as EchoPromise<DayPlanning[]>
  }

  @POST('/studenttemplates/{template_id}/rondes/{ronde_id}/dagplanningen/')
  addDagPlanningen (@Path('template_id') template_id: number,
              @Path('ronde_id') ronde_id: number, @Body() body: {}): EchoPromise<any> {
    return {} as EchoPromise<any>
  }

  @GET('/studenttemplates/{template_id}/dagplanningen/{dag_id}/')
  getDagPlanning (@Path('template_id') template_id: number,
              @Path('dag_id') dag_id: number): EchoPromise<DayPlanning> {
    return {} as EchoPromise<DayPlanning>
  }

  @PATCH('/studenttemplates/{template_id}/dagplanningen/{dag_id}/')
  editDagPlanning (@Path('template_id') template_id: number,
              @Path('dag_id') dag_id: number, @Body() body: {}): EchoPromise<any> {
    return {} as EchoPromise<any>
  }

  @DELETE('/studenttemplates/{template_id}/dagplanningen/{dag_id}/')
  deleteDagPlanning (@Path('template_id') template_id: number,
              @Path('dag_id') dag_id: number): EchoPromise<any> {
    return {} as EchoPromise<any>
  }

  @PATCH('/studenttemplates/{template_id}/dagplanningen/{dag_id}/eenmalig/')
  editDagPlanningEenmalig (@Path('template_id') template_id: number,
              @Path('dag_id') dag_id: number, @Body() body: {}): EchoPromise<any> {
    return {} as EchoPromise<any>
  }
}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .addInterceptor(new AuthInterceptor())
  .build(StudentTemplateService)
