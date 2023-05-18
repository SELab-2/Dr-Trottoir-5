import {mount} from '@vue/test-utils';
import TrashContainerCard from "@/components/containerTemplates/containers/TrashContainerCard.vue";
import TrashContainerCreate from "@/components/containerTemplates/containers/TrashContainerCreate.vue";
import TrashContainerEdit from "@/components/containerTemplates/containers/TrashContainerEdit.vue";
import TrashContainerHeader from "@/components/containerTemplates/containers/TrashContainerHeader.vue";
import {triggerInput} from "../../../utils/testHelper";
import TrashTemplateContainersList from "@/components/containerTemplates/containers/TrashTemplateContainersList.vue";


describe('trashContainerCard.vue', () => {

  let wrapper;

  beforeEach(() => {
    TrashContainerCard.beforeMount = jest.fn();
    TrashContainerCard.methods.editContainer = jest.fn();
    TrashContainerCard.methods.deleteContainer = jest.fn();
    wrapper = mount(TrashContainerCard, {
      propsData: {
        data: {
          trash_container: {
            collection_day: {
              day: 'Monday',
              start_hour: '10 AM',
              end_hour: '12 PM',
            },
            type: 'Type A',
          },
          extra_id: 1,
        },
      },
    });
  })

  it('renders the component correctly', () => {
    expect(wrapper.exists()).toBe(true);
    expect(TrashContainerCard.beforeMount).toBeCalled();

    expect(wrapper.find('.container-border').exists()).toBe(true);
    expect(wrapper.find('v-row[align="center"][justify="center"]').exists()).toBe(true);
    expect(wrapper.findAll('v-col').length).toBe(6);

    expect(wrapper.find('v-col:nth-child(1) p.text-style-title').text()).toBe('Monday');
    expect(wrapper.find('v-col:nth-child(2) p').text()).toBe('10 AM - 12 PM');
    expect(wrapper.find('v-col:nth-child(3) p').text()).toBe('Type A');

    expect(wrapper.find('v-col:nth-child(5) .button-style').exists()).toBe(true);
    expect(wrapper.find('v-col:nth-child(6) .button-style').exists()).toBe(true);
  });

  it('edit button is called', async () => {
    const editButton = wrapper.find('[data-test="edit"]');
    await editButton.trigger('click');
    expect(TrashContainerCard.methods.editContainer).toBeCalled();
  })

  it('delete button is called', async () => {
    const deleteButton = wrapper.find('[data-test="delete"]');
    await deleteButton.trigger('click');
    expect(TrashContainerCard.methods.deleteContainer).toBeCalled();
  })

})

describe('trashContainerCreate.vue', () => {

  let wrapper;

  beforeEach(() => {
    wrapper = mount(TrashContainerCreate);
  })

  it('renders the component correctly', () => {
    expect(wrapper.exists()).toBe(true);

    expect(wrapper.find('.justify-center.my-10').exists()).toBe(true);
    expect(wrapper.find('.text-h2').text()).toBe('Maak een nieuwe container aan');

    expect(wrapper.find('.my-10.py-5.mx-auto.w-75').exists()).toBe(true);
    expect(wrapper.find('v-form[fast-fail]').exists()).toBe(true);
    expect(wrapper.findAll('.justify-space-between.mx-auto v-col').length).toBe(4);

    expect(wrapper.find('v-col:nth-child(1) v-select[label="type container"]').exists()).toBe(true);
    expect(wrapper.find('v-col:nth-child(2) v-select[label="Dag van de week"]').exists()).toBe(true);
    expect(wrapper.find('v-col:nth-child(3) v-text-field[label="Beginuur"]').exists()).toBe(true);
    expect(wrapper.find('v-col:nth-child(4) v-text-field[label="Einduur"]').exists()).toBe(true);

    expect(wrapper.find('.overflow-hidden').text()).toBe('Aanmaken');
  });

  it('createContainer is called', async () => {
    TrashContainerCreate.methods.createContainer = jest.fn();
    wrapper = mount(TrashContainerCreate);
    const createButton = wrapper.find('.overflow-hidden');
    await createButton.trigger('click');
    expect(TrashContainerCreate.methods.createContainer).toBeCalled();
  })

  it('sets textfield values correctly', async () => {
    const beginUur = wrapper.find('v-col:nth-child(3) v-text-field[label="Beginuur"]');
    const eindUur = wrapper.find('v-col:nth-child(4) v-text-field[label="Einduur"]');

    const activator1 = (x) => {
      return {start_hour: x}
    }

    const activator2 = (x) => {
      return {end_hour: x}
    }
    beginUur.element.value = '10 AM';
    eindUur.element.value = '12 PM';

    await triggerInput(beginUur, wrapper, activator1);
    await triggerInput(eindUur, wrapper, activator2);

    expect(wrapper.vm.start_hour).toBe('10 AM');
    expect(wrapper.vm.end_hour).toBe('12 PM');
  })

  it('check v-select is rendered correctly', () => {
    const vSelects = wrapper.findAll('v-select');

    expect(vSelects.length).toBe(2);
  })

})

describe('trashContainerEdit.vue', () => {
  let wrapper;

  beforeEach(() => {
    TrashContainerEdit.beforeMount = jest.fn();
    wrapper = mount(TrashContainerEdit);
  })

  it('renders the component correctly', () => {
    expect(wrapper.exists()).toBe(true);

    expect(wrapper.find('.justify-center.my-10').exists()).toBe(true);
    expect(wrapper.find('.text-h2').text()).toBe('Pas de container aan');

    expect(wrapper.find('v-form[fast-fail]').exists()).toBe(true);
    expect(wrapper.findAll('.justify-space-between.mx-auto v-col').length).toBe(4);

    expect(wrapper.find('v-col:nth-child(1) v-select[label="containerType"]').exists()).toBe(true);
    expect(wrapper.find('v-col:nth-child(2) v-select[label="containerType"]').exists()).toBe(true);
    expect(wrapper.find('v-col:nth-child(3) v-text-field[label="Beginuur"]').exists()).toBe(true);
    expect(wrapper.find('v-col:nth-child(4) v-text-field[label="Einduur"]').exists()).toBe(true);

    expect(wrapper.find('.overflow-hidden').text()).toBe('Aanpassen');
  });

  it('editContainer is called', async () => {
    TrashContainerEdit.methods.editContainer = jest.fn();
    wrapper = mount(TrashContainerEdit);
    const createButton = wrapper.find('.overflow-hidden');
    await createButton.trigger('click');
    expect(TrashContainerEdit.methods.editContainer).toBeCalled();
  })

  it('sets textfield values correctly', async () => {
    const beginUur = wrapper.find('v-col:nth-child(3) v-text-field[label="Beginuur"]');
    const eindUur = wrapper.find('v-col:nth-child(4) v-text-field[label="Einduur"]');

    const activator1 = (x) => {
      return {start_hour: x}
    }

    const activator2 = (x) => {
      return {end_hour: x}
    }
    beginUur.element.value = '10 AM';
    eindUur.element.value = '12 PM';

    await triggerInput(beginUur, wrapper, activator1);
    await triggerInput(eindUur, wrapper, activator2);

    expect(wrapper.vm.start_hour).toBe('10 AM');
    expect(wrapper.vm.end_hour).toBe('12 PM');
  })

  it('check v-select is rendered correctly', () => {
    const vSelects = wrapper.findAll('v-select');

    expect(vSelects.length).toBe(2);
  })
})

describe('TrashContainerHeader', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = mount(TrashContainerHeader, {
      propsData: {
        round: true,
      },
    });
  });


  it('renders the component correctly', () => {
    expect(wrapper.exists()).toBe(true);

    expect(wrapper.find('.border').exists()).toBe(true);
    expect(wrapper.find('.col').exists()).toBe(true);
    expect(wrapper.findAll('.col').length).toBe(4);

    expect(wrapper.find('.col:nth-child(1) p[title="Dag"]').exists()).toBe(true);
    expect(wrapper.find('.col:nth-child(2) p[title="Uren"]').exists()).toBe(true);
    expect(wrapper.find('.col:nth-child(3) p[title="Type"]').exists()).toBe(true);

    expect(wrapper.find('.text-right').exists()).toBe(true);
    expect(wrapper.find('.text-right').text()).toBe('Acties');
  });

  it('sets the "round" prop correctly', async () => {
    expect(wrapper.props('round')).toBe(true);

    await wrapper.setProps({
      round: false,
    });

    expect(wrapper.props('round')).toBe(false);
  });
});


describe('TrashContainerTemplateList.vue', () => {

  let wrapper;

  beforeEach(() => {
    TrashTemplateContainersList.beforeMount = jest.fn();
    wrapper = mount(TrashTemplateContainersList);
  })


  it('renders the component correctly', () => {
    expect(wrapper.exists()).toBe(true);
    expect(TrashTemplateContainersList.beforeMount).toBeCalled();
  });

  it('renders the ListPage component with correct props', () => {
    const listPage = wrapper.find('[data-test="listPage"]');
    expect(listPage.exists()).toBe(true);
  });

  // component is empty in test environment waardoor er niet verder getest kan worden

});
