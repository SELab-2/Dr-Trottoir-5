import {mount} from '@vue/test-utils'
import CreateEditMailTemplate from '@/components/admin/mail/CreateEditMailTemplate.vue'
import SendMail from '@/components/admin/mail/SendMail.vue'
import {triggerInput} from "../../../../utils/testHelper";

describe('CreateEditMailTemplate.vue', () => {

  let wrapper;

  beforeEach(() => {
    wrapper = mount(CreateEditMailTemplate)
  })

  it('renders the component', () => {
    expect(wrapper.exists()).toBe(true);
  });

  it('Render title create', () => {
    expect(wrapper.find('h1').text()).toMatch('Mail template aanmaken')
  })

  it('Render title edit', async () => {
    await wrapper.setProps({edit: true})
    await wrapper.vm.$nextTick()
    expect(wrapper.find('h1').text()).toMatch('Mail template aanpassen')
  })

  it('sets the v-model for the textfield of the name of the template', async () => {

    const textField = wrapper.find('v-text-field')
    textField.element.value = 'test';
    const activator = (x) => {
      return {template: {name: x}}
    }
    triggerInput(textField, wrapper, activator)
    expect(wrapper.vm.$data.template.name).toBe('test');
  })

  it('sets the v-model for the textArea of the text of the template', async () => {
    const textArea = wrapper.find('v-textarea')
    textArea.element.value = 'Dit is een test mail template #test#';
    const activator = (x) => {
      return {template: {text: x}}
    }
    triggerInput(textArea, wrapper, activator)
    expect(wrapper.vm.$data.template.text).toBe('Dit is een test mail template #test#');
  })

  it('opens the dialog when the information icon is clicked', async () => {
    const infoIcon = wrapper.find('v-icon');
    infoIcon.trigger('click');
    await wrapper.vm.$nextTick();
    expect(wrapper.vm.showDialog).toBe(true);
  });

  it('test if createTemplate is called when the create button is clicked', async () => {
    CreateEditMailTemplate.methods.createTemplate = jest.fn()
    const wrapper = mount(CreateEditMailTemplate)
    await wrapper.setData({template: {name: 'test', text: 'Dit is een test mail template #test#'}})
    await wrapper.vm.$nextTick();

    const saveButton = wrapper.find('[data-test="create-button"]');
    await saveButton.trigger('click');
    await wrapper.vm.$nextTick();


    expect(CreateEditMailTemplate.methods.createTemplate).toHaveBeenCalled();
  });

  it('test if editTemplate is called when the edit button is clicked', async () => {
    CreateEditMailTemplate.methods.editTemplate = jest.fn()
    const wrapper = mount(CreateEditMailTemplate)
    await wrapper.setProps({edit: true})
    await wrapper.setData({template: {name: 'test', text: 'Dit is een test mail template #test#'}})
    await wrapper.vm.$nextTick();

    const saveButton = wrapper.find('[data-test="edit-button"]');
    await saveButton.trigger('click');
    await wrapper.vm.$nextTick();


    expect(CreateEditMailTemplate.methods.editTemplate).toHaveBeenCalled();
  });

  it('formats text correctly', () => {
    wrapper.setData({
      template: {
        name: 'Test Template',
        text: 'Hello #name#,<br>Test test<br>Best regards,<br>#syndicus#',
      }
    })

    expect(wrapper.vm.formattedText).toBe('Hello <b>name</b>,<br>Test test<br>Best regards,<br><b>syndicus</b>');
  });

  it('formats text correctly when there are no variables', () => {
    expect(wrapper.vm.formattedText).toBe('');
  })


})

describe('Sendmail.vue', () => {
  let wrapper;

  function initializeV_Autocomplete(wrapper) {
    wrapper.setData({
      templates: [
        {
          id: 1,
          name: 'Test template',
          text: 'Hello #name# #surname#'
        },
        {
          id: 2,
          name: 'Test template 2',
          text: 'Hello #name# #surname#'
        }]
    })
    const template = wrapper.vm.templates[0]
    const autocomplete = wrapper.find('v-autocomplete')
    wrapper.vm.$data.description = template.text
    autocomplete.wrapperElement._vei.onSlotchange.value(); // de onChange function als er een andere template wordt geselecteerd

  }

  beforeEach(() => {
    SendMail.mounted = jest.fn()
    wrapper = mount(SendMail)
  })

  it('renders the component', () => {
    expect(wrapper.exists()).toBe(true);
  });

  it('Render title create', () => {
    expect(wrapper.find('h1').text()).toMatch('Mail versturen')
  })

  it('Render sender label', () => {
    expect(wrapper.find('[data-test="aan"]').text()).toMatch('Aan')
  })

  it('Render name sender', () => {
    const testEmail = 'test@test.be'
    wrapper.setData({data: {syndicusEmail: testEmail}})
    expect(wrapper.find('v-text-field').text()).toMatch(testEmail)
  })

  it('Render template label', () => {
    expect(wrapper.find('[data-test="template"]').text()).toMatch('Template')
  })

  it('initialize argument fields when template is selected', async () => {
    initializeV_Autocomplete(wrapper)

    expect(wrapper.vm.$data.nameOfArguments).toStrictEqual(["#name#", "#surname#"])
    expect(wrapper.vm.$data.inputArguments).toStrictEqual(['', ''])


  })

  it('test when inputting data in the arguments', async () => {
    initializeV_Autocomplete(wrapper)

    let description = wrapper.vm.getDescriptionWithArguments()

    expect(description).toBe("Hello #name# #surname#")

    wrapper.vm.$data.inputArguments = ['test', '']
    description = wrapper.vm.getDescriptionWithArguments()

    expect(description).toBe("Hello test #surname#")
  })

  it('test formattedText function', () => {
    initializeV_Autocomplete(wrapper)
    wrapper.vm.$data.inputArguments = ['test', '']

    expect(wrapper.vm.formattedText).toBe("Hello test <b>surname</b>")
  })

  it('test if sendMail is called when the send button is clicked', async () => {
    SendMail.methods.sendMail = jest.fn()
    const wrapper = mount(SendMail)
    const button = wrapper.find('[data-test="send-button"]');
    button.trigger('click');
    await wrapper.vm.$nextTick();
    expect(SendMail.methods.sendMail).toHaveBeenCalled();
  })

  it('getMailbody', () => {
    initializeV_Autocomplete(wrapper)
    wrapper.vm.$data.inputArguments = ['test', 'test2']
    const date = new Date()
    wrapper.setProps({data: {syndicusEmail: 'test@test.be', post: {timeStamp: date, imageURL: '', description: 'test2'}}})
    expect(wrapper.vm.getMailBody()).toBeTruthy()
  })



})
