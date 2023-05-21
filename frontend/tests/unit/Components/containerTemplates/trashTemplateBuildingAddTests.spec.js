import {mount} from '@vue/test-utils';
import TrashTemplateBuildingAdd from "@/components/containerTemplates/buildings/TrashTemplateBuildingAdd.vue";
import TrashTemplateBuildingCard from "@/components/containerTemplates/buildings/TrashTemplateBuildingCard.vue";
import TrashTemplateBuildingEdit from "@/components/containerTemplates/buildings/TrashTemplateBuildingEdit.vue";
import TrashTemplateBuildingHeader from "@/components/containerTemplates/buildings/TrashTemplateBuildingHeader.vue";
import TrashTemplateBuildingsList from "@/components/containerTemplates/buildings/TrashTemplateBuildingsList.vue";

describe('TrashTemplateBuildingAdd.vue', () => {

  let wrapper;

  beforeEach(() => {
    TrashTemplateBuildingAdd.beforeMount = jest.fn();
    wrapper = mount(TrashTemplateBuildingAdd)
  });

  it('render', () => {
    expect(wrapper.exists()).toBe(true);
    expect(TrashTemplateBuildingAdd.beforeMount).toBeCalled();
  })

  it('initializes data correctly', () => {
    expect(wrapper.vm.building_options).toEqual([]);
    expect(wrapper.vm.building_chosen).toEqual([]);
    expect(wrapper.vm.building_originals).toEqual([]);
    expect(wrapper.vm.status).toBe('I');
  });

  it('redenders the component correctly', () => {
    expect(wrapper.find('div[class="text-h2"]').text()).toBe("Kies gebouwen voor deze template");
    expect(wrapper.find('v-select[label="Gekozen gebouwen"]').exists()).toBe(true);
  })

})

describe('TrashTemplateBuildingCard.vue', () => {
  let wrapper;

  beforeEach(() => {
    TrashTemplateBuildingCard.mounted = jest.fn();
    TrashTemplateBuildingCard.beforeMount = jest.fn();
    TrashTemplateBuildingCard.methods.downloadDocument = jest.fn();
    TrashTemplateBuildingCard.methods.goToBuildingPage = jest.fn();

    wrapper = mount(TrashTemplateBuildingCard, {
      data: () => ({
        building: {
          id: 1,
          name: 'Building Name',
          adres: 'Building Address',
          efficiency: 80,
          manual: {
            id: 1,
            manualStatus: 'Klaar',
            file: 'manual.pdf',
          },
        },
        status: 'I',
      })
    });


  });


  it('renders the component correctly', () => {
    expect(wrapper.exists()).toBe(true);
    expect(TrashTemplateBuildingCard.beforeMount).toBeCalled();
    expect(wrapper.find('span').text()).toBe('I');
  })

  it('display the correct building data', () => {
    const building = wrapper.findAll('p');
    expect(building.at(0).text()).toBe('Building Name');
    expect(building.at(1).text()).toBe('Building Address');
    expect(building.at(2).text()).toBe('80%');
  })

  it('downloadDocument method is called', async () => {
    const downloadButton = wrapper.find('[value="download"]');
    await downloadButton.trigger('click');
    expect(TrashTemplateBuildingCard.methods.downloadDocument).toBeCalled();
  });

  it('goToBuildingPage method is called', async () => {
    const goToBuildingPageButton = wrapper.find('p[class="text-style-building"]');
    await goToBuildingPageButton.trigger('click');
    expect(TrashTemplateBuildingCard.methods.goToBuildingPage).toBeCalled();
  });

})


describe('TrashTemplateBuildingEdit.vue', () => {

  let wrapper;

  beforeEach(() => {
    const building = {
      name: 'Building Name',
      adres: 'Building Address',
    }

    TrashTemplateBuildingEdit.beforeMount = jest.fn();

    wrapper = mount(TrashTemplateBuildingEdit, {
      data: () => ({
        building: {building: building},
      })
    });
  })

  it('renders the component correctly', () => {
    expect(wrapper.exists()).toBe(true);
    expect(TrashTemplateBuildingEdit.beforeMount).toBeCalled();
    expect(wrapper.find('div[class="text-h2"]').text()).toBe('Pas de containers van dit gebouw aan.');
    expect(wrapper.find('v-select[label="Kies containers voor dit gebouw"]').exists()).toBe(true);
  })

  it('renders the correct building data', () => {
    const building = wrapper.findAll('p');
    expect(building.at(0).text()).toBe('Building Name');
    expect(building.at(1).text()).toBe('Building Address');
  })
})

describe('TrashTemplateBuildingHeader.vue', () => {

  let wrapper;

  beforeEach(() => {
    wrapper = mount(TrashTemplateBuildingHeader)
  })

  it('renders the component', () => {
    expect(wrapper.exists()).toBe(true);
  });

  it('renders the correct elements', () => {
    expect(wrapper.find('v-container').exists()).toBe(true);
    expect(wrapper.find('v-row').exists()).toBe(true);
    expect(wrapper.findAll('v-col').length).toBe(6);
    expect(wrapper.find('p[title="Gebouw"]').exists()).toBe(true);
    expect(wrapper.find('p[title="Adres"]').exists()).toBe(true);
    expect(wrapper.find('p[title="Efficiëntie"]').exists()).toBe(true);
    expect(wrapper.find('p[title="Handleiding"]').exists()).toBe(true);
  });

  it('renders the "Efficiëntie" element based on the "round" prop', async () => {
    const wrapperWithRoundProp = mount(TrashTemplateBuildingHeader, {
      propsData: {round: true},
    });
    const wrapperWithoutRoundProp = mount(TrashTemplateBuildingHeader, {
      propsData: {round: false},
    });

    expect(wrapperWithRoundProp.find('p[title="Efficiëntie"]').exists()).toBe(false);
    expect(wrapperWithoutRoundProp.find('p[title="Efficiëntie"]').exists()).toBe(true);
  });
})

describe('TrashTemplateBuildingsList.vue', () => {

  let wrapper;
  beforeEach(() => {
    TrashTemplateBuildingsList.beforeMount = jest.fn();
    wrapper = mount(TrashTemplateBuildingsList)
  })

  it('renders the component', () => {
    expect(wrapper.exists()).toBe(true);
    expect(TrashTemplateBuildingsList.beforeMount).toBeCalled();
  })

  it('renders the ListPage component with correct props', () => {
    const listPage = wrapper.find('[data-test="listPage"]');
    expect(listPage.exists()).toBe(true);
  });
})
