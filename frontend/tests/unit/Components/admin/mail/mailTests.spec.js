import { mount } from '@vue/test-utils'
import CreateEditMailTemplate from '@/components/admin/mail/CreateEditMailTemplate.vue'

describe('CreateEditMailTemplate.vue', () => {

  let wrapper;

  beforeEach(() => {
    wrapper = mount(CreateEditMailTemplate);
  })


  it('Render title create', () => {
    expect(wrapper.find('h1').text()).toMatch('Mail template aanmaken')
  })

  it('Render title edit', async () => {
    wrapper.setProps({ edit: true })
    await wrapper.vm.$nextTick()
    expect(wrapper.find('h1').text()).toMatch('Mail template aanpassen')
  })

  it('sets the v-model of v-text-field for the name of the mail template',  () => {
    const textField = wrapper.find('v-text-field')
    textField.element.value = 'test';
    textField.trigger('input');
  })



})
