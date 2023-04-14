import {
  Body,
  EchoPromise,
  EchoService,
  EchoServiceBuilder,
  POST,
} from "@/api/EchoFetch";

import MailTemplate from "@/api/models/MailTemplate";
import config from "@/config";
import {InputFields} from "@/types/fields/InputFields";

class MailTemplateService extends EchoService {

  /**
   * Create new mail template
   */
  @POST("/mailtemplates/")
  createMailTemplate(@Body() body: InputFields): EchoPromise<MailTemplate> {
    return {} as EchoPromise<MailTemplate>
  }




}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .build(MailTemplateService);
