import Unauthorized from '../../../src/views/Unauthorized.vue';
import {mount} from "@vue/test-utils";
import NormalButton from "@/components/NormalButton.vue";
import { createRouter, createWebHistory } from 'vue-router';

describe("Unauthorized.vue", () => {

  let wrapper;
  let mockRouter;

  beforeEach(() => {
    mockRouter = createRouter({
      history: createWebHistory(),
      routes: [],
    });
    mockRouter.back = jest.fn()
    jest.mock('vue-router', () => ({
      createRouter: jest.fn(() => mockRouter),
      createWebHistory: jest.fn()
    }));
    wrapper = mount(Unauthorized);
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

  it('normal button with go back triggr',  () => {
    wrapper.findComponent(NormalButton).trigger('click');
    expect(mockRouter.back()).toHaveBeenCalled();
  })

});
