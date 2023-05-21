import { mount } from '@vue/test-utils';
import HomeView from "@/views/HomeView.vue";
import Unauthorized from "@/views/Unauthorized.vue";

describe('HomeView', () => {


  it('create is called when component is mounted', () => {
    HomeView.created = jest.fn();
    mount(HomeView);
    expect(HomeView.created).toHaveBeenCalled();
  })

  it('renders the correct', () => {
    HomeView.created = jest.fn();
    const wrapper = mount(HomeView);
    expect(wrapper.exists()).toBe(true);
  })

});

describe('Unauthorized.vue', () => {

  let wrapper;

  beforeEach(() => {
    wrapper = mount(Unauthorized);
  })

  it('renders the correct', () => {
    expect(wrapper.exists()).toBe(true);
  })

  it('displays the "Unauthorized" message', () => {
    const message = wrapper.find('.mx-1');
    expect(message.text()).toBe('Geen toegang!');
  });

  it('goBack is called when button is clicked', async () => {
    Unauthorized.methods.goBack = jest.fn();
    wrapper = mount(Unauthorized);
    const button = await wrapper.find('[data-test="goBack"]');
    await button.trigger('click');
    expect(Unauthorized.methods.goBack).toHaveBeenCalled();
  })

  it('renders the component correctly', async() => {
    const divs = wrapper.findAll('div[class="mx-1"]');
    expect(divs.at(0).text()).toBe('Geen toegang!');
    expect(divs.at(1).text()).toBe('U heeft onvoldoende rechten om deze pagina te bezoeken.');
  })

})


