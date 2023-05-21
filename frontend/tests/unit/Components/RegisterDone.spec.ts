import {mount} from "@vue/test-utils"
import RegisterDone from "@/components/RegisterDone.vue"

describe('RegisterDone.vue', () => {

  let wrapper;

  beforeEach(() => {
    wrapper = mount(RegisterDone);
  })

  it('render of component', () => {
    expect(wrapper.exists()).toBeTruthy()
  })

  it('check for succes text', () => {
    const div = wrapper.find('[data-test="succes"]');
    expect(div.text()).toBe('Registratie is gelukt!')
  })

  it('check for thank you text', () => {
    const div = wrapper.find('[data-test="thank-you"]');
    expect(div.text()).toBe('Bedankt voor het registreren bij Dr. Trottoir.');
  })

  it('check for waiting text', () => {
    const div = wrapper.find('[data-test="waiting"]');
    expect(div.text()).toBe('Als uw aanmelding is verwerkt, zal de applicatie hier beschikbaar zijn.');
  })

})
