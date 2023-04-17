import {EchoPromise, EchoService, EchoServiceBuilder, GET} from "@/api/EchoFetch";
import StudentTemplate from "@/api/models/StudentTemplate";
import config from "@/config";
import {AuthInterceptor} from "@/api/interceptors/AuthInterceptor";

class StudentTemplateService extends EchoService {

@GET("/studenttemplates/")
  getStudentTemplates(): EchoPromise<StudentTemplate[]> {
    return {} as EchoPromise<StudentTemplate[]>;
  }
}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .addInterceptor(new AuthInterceptor())
  .build(StudentTemplateService);
