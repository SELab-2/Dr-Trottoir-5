import nock from "nock";
import MailTemplateService from "@/api/services/MailTemplateService";
import MailTemplate from "@/api/models/MailTemplate";
import { InputFields } from "@/types/fields/InputFields";

const MOCK_SERVER_URL = "http://localhost:8000/api";
jest.mock("@/api/services/MailTemplateService");
describe('MailTemplateService', () => {
  afterEach(() => {
    nock.cleanAll();
  });

  it('createMailTemplate', async () => {
    MailTemplateService.createMailTemplate = jest.fn();
  //MailTemplateService.createMailTemplate.mockResolvedValue(new MailTemplate());
    const template = new InputFields();

    const expectedResponse = new MailTemplate();
    expectedResponse.id = 1;
    expectedResponse.name = 'test-template';
    expectedResponse.content = 'test';

    const scope = nock(MOCK_SERVER_URL)
      .post('/mailtemplates', template)
      .reply(200, expectedResponse);

    const response = MailTemplateService.createMailTemplate(template);

    expect(response).toEqual(expectedResponse);
    expect(scope.isDone()).toBeTruthy();
  });

});
