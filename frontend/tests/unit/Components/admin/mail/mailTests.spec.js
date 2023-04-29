import { mount } from '@vue/test-utils'
import CreateEditMailTemplate from '@/components/admin/mail/CreateEditMailTemplate.vue'

describe('CreateEditMailTemplate.vue', () => {

  it('Render title create', () => {
    const wrapper = mount(CreateEditMailTemplate, {
      props: {
        edit: false
      }
    })
    expect(wrapper.find('h1').text()).toMatch('Mail template aanmaken')
  })



})
