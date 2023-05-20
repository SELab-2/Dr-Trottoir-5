import { mount } from '@vue/test-utils'
import CreateBuildingView from '@/views/admin/CreateBuildingView.vue'

describe('CreateBuildingView.vue', () => {

  let wrapper;

  beforeEach(() => {
    CreateBuildingView.beforeMount = jest.fn();
    wrapper = mount(CreateBuildingView);
  })

  it('renders the correct', () => {
    expect(wrapper.exists()).toBe(true);
    expect(CreateBuildingView.beforeMount).toHaveBeenCalled();
  })

  it('initializes the data properties correctly', () => {
    expect(wrapper.vm.name).toBe('');
    expect(wrapper.vm.adres).toBe('');
    expect(wrapper.vm.klant_nr).toBe(null);
    expect(wrapper.vm.file).toBe(null);
    expect(wrapper.vm.smallScreen).toBe(false);
    expect(wrapper.vm.locations).toEqual([]);
    expect(wrapper.vm.selectedLocation).toBe(null);
    expect(wrapper.vm.errors).toBe(null);
  });

  it('call createBuilding when form is submitted', async () => {
    CreateBuildingView.methods.createBuilding = jest.fn();
    wrapper = mount(CreateBuildingView);
    const button = wrapper.find('[date-test="create"]');
    await button.trigger('click');
    expect(CreateBuildingView.methods.createBuilding).toHaveBeenCalled();
  })

  it('renders the component correctly', async() => {
    expect(wrapper.find('h1').text()).toBe('Nieuw gebouw aanmaken');
    expect(wrapper.find('v-select[label="Locatie"]').exists()).toBeTruthy();
    expect(wrapper.find('v-text-field[label="Klanten nummer"]').exists()).toBeTruthy();
    expect(wrapper.find('v-file-input[label="Handleiding"]').exists()).toBeTruthy();
  })
})
