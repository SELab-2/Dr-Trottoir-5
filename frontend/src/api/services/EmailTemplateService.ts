import {EchoPromise, EchoService, EchoServiceBuilder, GET, Path} from "@/api/EchoFetch";
import config from "@/config";
import {AuthInterceptor} from "@/api/interceptors/AuthInterceptor";
import EmailTemplate from "@/api/models/EmailTemplate";

class EmailTemplateService extends EchoService {

  /**
   * Get emailTemplate information
   */
  @GET('/mailtemplates/')
  getEmailTemplates(): EchoPromise<EmailTemplate[]> {
    return {} as EchoPromise<EmailTemplate[]>
  }
}


export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .addInterceptor(new AuthInterceptor())
  .build(EmailTemplateService);
