import {
  Body,
  EchoPromise,
  EchoService,
  EchoServiceBuilder,
  POST, GET, PATCH, Path
} from '@/api/EchoFetch'

import MailTemplate from '@/api/models/MailTemplate'
import config from '@/config'
import { InputFields } from '@/types/fields/InputFields'

class MailTemplateService extends EchoService {
  /**
   * Create new mail template
   */
  @POST('/mailtemplates/')
  createMailTemplate (@Body() body: InputFields): EchoPromise<MailTemplate> {
    return {} as EchoPromise<MailTemplate>
  }

  /**
   * Get mail template by id
   */

  @GET('/mailtemplates/{id}/')
  getMailTemplate (@Path('id') id: number): EchoPromise<MailTemplate> {
    return {} as EchoPromise<MailTemplate>
  }

  /**
   * Get all mail templates
   */

  @GET('/mailtemplates/')
  getMailTemplates (): EchoPromise<MailTemplate[]> {
    return {} as EchoPromise<MailTemplate[]>
  }

  /**
   * Update mail template
   */
  @PATCH('/mailtemplates/{id}/')
  updateMailTemplate (@Path('id') id: number, @Body() body: InputFields): EchoPromise<MailTemplate> {
    return {} as EchoPromise<MailTemplate>
  }
}

export default new EchoServiceBuilder()
  .setBaseUrl(config.BACKEND.URL)
  .build(MailTemplateService)
