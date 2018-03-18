d3.json('data/total_users.json', data => {
  data = MG.convert.date(data, 'date', '%Y-%m-%dT%H:%M:%SZ')
  MG.data_graphic({
    title: "Total Users",
    data: data,
    full_width: true,
    height: 300,
    target: '#total-users',
    y_accessor: 'total'
  })
})

var new_users = {
  title: "New Users",
  full_width: true,
  height: 300,
  target: '#new-users',
  y_accessor: 'total',
  transition_on_update: false
}

d3.json('data/new_users/day.json', data => {
  data = MG.convert.date(data, 'date', '%Y-%m-%dT%H:%M:%SZ')
  new_users.data = data
  MG.data_graphic(new_users)
})

$('#new-users-controls button').click(function () {
  $(this).addClass('active').siblings().removeClass('active')

  var period = $(this).data('period')
  d3.json(`data/new_users/${period}.json`, data => {
    data = MG.convert.date(data, 'date', '%Y-%m-%dT%H:%M:%SZ')
    new_users.data = data
    MG.data_graphic(new_users)
  })
})
