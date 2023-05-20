import {mount} from '@vue/test-utils'
import TrashContainerTemplateCard from "@/components/containerTemplates/TrashContainerTemplateCard.vue";
import TrashContainerTemplateList from "@/components/containerTemplates/TrashContainerTemplateList.vue";
import TrashContainerTemplateCreate from "@/components/containerTemplates/TrashContainerTemplateCreate.vue";
import TrashContainerTemplateEdit from "@/components/containerTemplates/TrashContainerTemplateEdit.vue";
import {triggerInput} from "../../../utils/testHelper";
import TrashContainerTemplateHeader from "@/components/containerTemplates/TrashContainerTemplateHeader.vue";

describe('trashContainerTemplateCard.vue', () => {

  let wrapper;

  beforeEach(() => {
    TrashContainerTemplateCard.beforeMount = jest.fn();
    wrapper = mount(TrashContainerTemplateCard, {
      propsData: {
        data: {
          id: 1,
          name: 'Template 1',
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


describe('trashContainerTemplateCreate.vue', () => {

  let wrapper;

  beforeEach(() => {
    TrashContainerTemplateCreate.beforeMount = jest.fn();
    wrapper = mount(TrashContainerTemplateCreate);
  })

  it('renders the component correctly', () => {
    expect(wrapper.exists()).toBe(true);
    expect(TrashContainerTemplateCreate.beforeMount).toBeCalled();
  })

  it('sets textfield correctly', async () => {
    const textField = wrapper.find('v-text-field');
    textField.element.value = 'test';
    const activator = (x) => {
      return {name: x}
    }
    await triggerInput(textField, wrapper, activator);
    expect(wrapper.vm.name).toBe('test');
    expect(textField.attributes('label')).toBe('Naam');
  })

  it('sets checkbox correctly', async () => {
    const checkbox = wrapper.find('v-checkbox');
    const activator = (x) => {
      return {even: x}
    }
    expect(wrapper.vm.even).toBe(true);
    checkbox.element.value = false;
    triggerInput(checkbox, wrapper, activator);
    expect(wrapper.vm.even).toBe(false);
    expect(checkbox.attributes('label')).toBe('Even');
  })

  it('create button is called', async () => {
    TrashContainerTemplateCreate.methods.create = jest.fn();
    wrapper = mount(TrashContainerTemplateCreate);
    const createButton = wrapper.find('[data-test="create"]');
    await createButton.trigger('click');
    expect(TrashContainerTemplateCreate.methods.create).toBeCalled();
  })

  it('v-select exists', () => {
    const vSelect = wrapper.find('v-select');
    expect(vSelect.exists()).toBeTruthy()

    expect(vSelect.attributes('label')).toBe('Locatie');
  })
})

describe('trashContainerTemplateEdit.vue', () => {
  let wrapper;

  beforeEach(() => {
    TrashContainerTemplateEdit.beforeMount = jest.fn();
    wrapper = mount(TrashContainerTemplateEdit)
  })

  it('renders the component correctly', () => {
    expect(wrapper.exists()).toBe(true);
    expect(TrashContainerTemplateEdit.beforeMount).toBeCalled();
  })

  it('sets textfield correctly', async () => {
    const textField = wrapper.find('v-text-field');
    textField.element.value = 'test';
    const activator = (x) => {
      return {name: x}
    }
    await triggerInput(textField, wrapper, activator);
    expect(wrapper.vm.name).toBe('test');
    expect(textField.attributes('label')).toBe('Naam');
  })

  it('sets checkbox correctly', async () => {
    const checkbox = wrapper.find('v-checkbox');

    const activator = (x) => {
      return {even: x}
    }
    expect(wrapper.vm.even).toBe(true);
    checkbox.element.value = false;
    triggerInput(checkbox, wrapper, activator);
    expect(wrapper.vm.even).toBe(false);
    expect(checkbox.attributes('label')).toBe('Even');

  })

  it('v-select exists', () => {
    const vSelect = wrapper.find('v-select');
    expect(vSelect.attributes('label')).toBe('Locatie');
  })
})

describe('TrashContainerTemplateHeader.vue', () => {

  let wrapper;

  beforeEach(() => {
    wrapper = mount(TrashContainerTemplateHeader);
  })

  it('renders the component correctly with the right text', () => {
    expect(wrapper.exists()).toBe(true);

    expect(wrapper.find('v-container.border').exists()).toBe(true);
    expect(wrapper.find('v-row[align="center"][justify="center"]').exists()).toBe(true);
    expect(wrapper.findAll('v-col.col').length).toBe(6);

    expect(wrapper.find('v-col.col:nth-child(1) p[title="Naam"]').text()).toBe('Naam');
    expect(wrapper.find('v-col.col:nth-child(2) p[title="Vuilnisbakken"]').text()).toBe('Vuilnisbakken');
    expect(wrapper.find('v-col.col:nth-child(3) p[title="Gebouwen"]').text()).toBe('Gebouwen');
    expect(wrapper.find('v-col.col:nth-child(4) p[title="Jaar"]').text()).toBe('Status');
    expect(wrapper.find('v-col.col:nth-child(5) p[title="Locatie"]').text()).toBe('Locatie');
    expect(wrapper.find('v-col.col:nth-child(6) p[title="Even"]').text()).toBe('Even');
    expect(wrapper.find('v-col.text-right').text()).toBe('Acties');

    expect(wrapper.props().round).toBe(false);

    expect(wrapper.vm.$options.name).toBe('TrashContainerTemplateHeader');
  });

})
