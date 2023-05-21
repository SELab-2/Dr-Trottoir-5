import {mount} from "@vue/test-utils";
import BuildingCard from "@/components/admin/BuildingCard.vue";

describe('BuildingCard.vue', () => {

  let wrapper

  beforeEach(async () => {
    BuildingCard.beforeMount = () => Promise.resolve();
    BuildingCard.methods.downloadDocument = jest.fn()
    BuildingCard.methods.goToEditBuilding = jest.fn()
    BuildingCard.methods.deletePost = jest.fn();
    wrapper = mount(BuildingCard, {
      props: {
        data: {
          name: 'Test Gebouw',
          adres: 'TestStraat 1',
          id: 0,
          ivago_klantnr: 0,
          buildingID: '',
          manual: null,
          containers: null,
          location: null
        }
      }
    });
  });

  it('render of component', async () => {
    expect(wrapper.exists()).toBeTruthy();
  })

  it('check for name', () => {
    expect(wrapper.find('[data-test="name"]').text()).toBe('Test Gebouw');
  });

  it('check for adress', () => {
    expect(wrapper.find('[data-test="adres"]').text()).toBe('TestStraat 1');
  });

  it('check for manual', () => {
    expect(wrapper.find('[data-test="manual"]').text()).toBe('Handleiding');
  });

  it('download manual', async () => {
    const manualMenu = wrapper.find('[data-test="manual"]');
    await manualMenu.trigger('click');
    await wrapper.vm.$nextTick();
    expect(BuildingCard.methods.downloadDocument).toHaveBeenCalled();
  });

  it('go to edit page', async () => {
    const editButton = wrapper.find('[data-test="edit"]');
    await editButton.trigger('click');
    await wrapper.vm.$nextTick();
    expect(BuildingCard.methods.goToEditBuilding).toHaveBeenCalled();
  });

  it('delete building', async () => {
    const editButton = wrapper.find('[data-test="delete"]');
    await editButton.trigger('click');
    await wrapper.vm.$nextTick();
    expect(BuildingCard.methods.deletePost).toHaveBeenCalled();
  });

})
