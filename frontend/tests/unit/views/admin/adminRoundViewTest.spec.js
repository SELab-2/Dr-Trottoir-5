import { mount } from '@vue/test-utils'
import AdminRoundView from '@/views/admin/AdminRoundView.vue'

describe('AdminRoundView.vue', () => {
  let wrapper;
  beforeEach(() => {
    AdminRoundView.created = jest.fn();
    wrapper = mount(AdminRoundView);
  })

  it('renders the correct', () => {
    expect(wrapper.exists()).toBe(true);
    expect(AdminRoundView.created).toHaveBeenCalled();
  })

  it('sets initial data correctly', () => {
    const initialData = wrapper.vm.$data;
    expect(initialData.date).toBeNull();
    expect(initialData.dateString).toBe('');
    expect(initialData.planning).toBeNull();
    expect(initialData.pictures).toBeNull();
    expect(initialData.duration).toBeNull();
    expect(initialData.template).toBeNull();
    expect(initialData.status).toBe('Niet voltooid');
  });

  it('renders the component correctly', async() => {
    const wrapper = mount(AdminRoundView, {
      data() {
        return {
          planning: {
            students: [
              { id: 1, first_name: 'John', last_name: 'Doe' },
              { id: 2, first_name: 'Jane', last_name: 'Smith' },
            ],
            ronde:{name: 'Ronde 1'}
          },
          pictures: [],
        };
      },
    });

    await wrapper.vm.$forceUpdate();
    const studentNames = wrapper.findAll('h2');
    expect(studentNames.length).toBe(2);
    expect(studentNames[0].text()).toBe('John Doe');
    expect(studentNames[1].text()).toBe('Jane Smith');

    expect(wrapper.find('h1').text()).toBe('Ronde Ronde 1 op  door');

    const titles = wrapper.findAll('h5');
    expect(titles.at(0).text()).toBe('Gebouw');
    expect(titles.at(1).text()).toBe('Status');
    expect(titles.at(2).text()).toBe('Opmerkingen');
    expect(titles.at(3).text()).toBe('Tijd');
    expect(titles.at(4).text()).toBe('Locatie');
  });

})
