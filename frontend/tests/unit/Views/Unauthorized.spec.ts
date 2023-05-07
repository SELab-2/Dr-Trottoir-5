import Unauthorized from '../../../src/views/Unauthorized.vue';
import {shallowMount} from "@vue/test-utils";
import NormalButton from "@/components/NormalButton.vue";

describe("Unauthorized.vue", () => {

  let wrapper;

  beforeEach(() => {
    wrapper = shallowMount(Unauthorized);
  });

  it('render the component', () => {
    expect(wrapper.exists()).toBeTruthy();
  })

  it('icon of unauthorized present', () => {
    expect(wrapper.find('v-icon').attributes('icon')).toBe("mdi-cancel");
  });

  it('text geen toegang', () => {
    expect(wrapper.findAll('div').filter(div => div.text() === 'Geen toegang!').length).toBe(1);
  });

  it('text permission', () => {
    expect(wrapper.findAll('div')
      .filter(div => div.text() === 'U heeft onvoldoende rechten om deze pagina te bezoeken.')
      .length).toBe(1);
  })

  it('normal button with go back exist', () => {
    expect(wrapper.findComponent(NormalButton).exists()).toBeTruthy();
  })


});
