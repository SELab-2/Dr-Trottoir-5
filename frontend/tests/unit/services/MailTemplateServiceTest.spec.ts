import nock from "nock";
import MailTemplateService from "@/api/services/MailTemplateService";
import MailTemplate from "@/api/models/MailTemplate";

const MOCK_SERVER_URL = "http://localhost:8000/api";

describe('MailTemplateService', () => {
  afterEach(() => {
    nock.cleanAll();
  });

  it('createMailTemplate', async () => {
    const template = new MailTemplate();
    template.name = 'test-template';
    template.content = 'test';

    const expectedResponse = new MailTemplate();
    expectedResponse.id = 1;
    expectedResponse.name = 'test-template';
    expectedResponse.content = 'test';

    const scope = nock(MOCK_SERVER_URL)
      .post('/mailtemplates', template)
      .reply(200, expectedResponse);

    const service = MailTemplateService;
    const response = await service.createMailTemplate(template);

    expect(response).toEqual(expectedResponse);
    expect(scope.isDone()).toBeTruthy();
  });

});
