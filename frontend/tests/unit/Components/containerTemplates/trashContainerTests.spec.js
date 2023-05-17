import {mount} from '@vue/test-utils'
import TrashContainerTemplateCard from "@/components/containerTemplates/TrashContainerTemplateCard.vue";
import TrashContainerTemplateList from "@/components/containerTemplates/TrashContainerTemplateList.vue";

describe('trashContainerTemplateCard.vue', () => {

  let wrapper;

  beforeEach(() => {
    TrashContainerTemplateCard.beforeMount = jest.fn();
    wrapper = mount(TrashContainerTemplateCard, {
      propsData: {
        data: {
          id: 1,
          name: 'Template 1',
          year: 2023,
          week: 20,
          location: 1,
          even: true,
        }
      }
    });
  })

  it('render', () => {
    expect(wrapper.exists()).toBe(true);
    expect(TrashContainerTemplateCard.beforeMount).toBeCalled();
  })

  it('displays the props', () => {
    expect(wrapper.find('p').text()).toBe('Template 1');
    expect(wrapper.find('[data-test="year"]').text()).toBe("2023");
    expect(wrapper.find('[data-test="week"]').text()).toBe("20");
    expect(wrapper.find('[data-test="even"]').text()).toBe("true");
  });

  it('displays the data', async () => {
    await wrapper.setData({locatie: "1"})
    await wrapper.vm.$nextTick();
    expect(wrapper.find('[data-test="location"]').text()).toBe("1");
  })

  it('check methods are called', async () => {
    TrashContainerTemplateCard.methods.goToTrashTemplateContainersPage = jest.fn();
    TrashContainerTemplateCard.methods.goToTrashTemplateBuildingsPage = jest.fn();
    TrashContainerTemplateCard.methods.editTemplate = jest.fn();
    TrashContainerTemplateCard.methods.deleteTemplate = jest.fn();

    wrapper = mount(TrashContainerTemplateCard, {
      propsData: {
        data: {
          id: 1,
          name: 'Template 1',
          year: 2023,
          week: 20,
          location: 1,
          even: true,
        }
      }
    });

    const goToTrashTemplateContainersPageButton = wrapper.find('[data-test="goToTrashTemplateContainersPage"]');
    const goToTrashTemplateBuildingsPageButton = wrapper.find('[data-test="goToTrashTemplateBuildingsPage"]');
    const editTemplateButton = wrapper.find('[data-test="editTemplate"]');
    const deleteTemplateButton = wrapper.find('[data-test="deleteTemplate"]');


    await goToTrashTemplateContainersPageButton.trigger('click');
    expect(TrashContainerTemplateCard.methods.goToTrashTemplateContainersPage).toBeCalled();
    await goToTrashTemplateBuildingsPageButton.trigger('click');
    expect(TrashContainerTemplateCard.methods.goToTrashTemplateBuildingsPage).toBeCalled();
    await editTemplateButton.trigger('click');
    expect(TrashContainerTemplateCard.methods.editTemplate).toBeCalled();
    await deleteTemplateButton.trigger('click');
    expect(TrashContainerTemplateCard.methods.deleteTemplate).toBeCalled();
  })

  describe('TrashContainerTemplateList.vue', () => {

    let wrapper;

    beforeEach(() => {
      TrashContainerTemplateList.beforeMount = jest.fn();
      wrapper = mount(TrashContainerTemplateList);
    })


    it('renders the component correctly', () => {
      expect(wrapper.exists()).toBe(true);
      expect(TrashContainerTemplateList.beforeMount).toBeCalled();
    });

    it('renders the ListPage component with correct props', () => {
      const listPage = wrapper.find('[data-test="listPage"]');
      expect(listPage.exists()).toBe(true);
    });

    // component is empty in test environment waardoor er niet verder getest kan worden

  });

})
