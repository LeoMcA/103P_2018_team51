const DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

d3.json('data/total_users.json', data => {
  data = MG.convert.date(data, 'date', DATE_FORMAT)
  MG.data_graphic({
    title: "Total Users",
    data: data,
    interpolate: d3.curveLinear,
    full_width: true,
    height: 300,
    target: '#total-users',
    y_accessor: 'total'
  })
})

var new_users = {
  title: "New Users",
  interpolate: d3.curveLinear,
  full_width: true,
  height: 300,
  target: '#new-users',
  y_accessor: 'total',
  transition_on_update: false
}

d3.json('data/new_users/day.json', data => {
  data = MG.convert.date(data, 'date', DATE_FORMAT)
  new_users.data = data
  MG.data_graphic(new_users)
})

$('#new-users-controls button').click(function () {
  $(this).addClass('active').siblings().removeClass('active')

  var period = $(this).data('period')
  d3.json(`data/new_users/${period}.json`, data => {
    data = MG.convert.date(data, 'date', DATE_FORMAT)
    new_users.data = data
    MG.data_graphic(new_users)
  })
})

d3.json('data/events.json', data => {
  for (var i = 0; i < data.length; i++) {
    data[i] = MG.convert.date(data[i], 'date', DATE_FORMAT)
  }
  MG.data_graphic({
    title: "Engagement: All Events",
    data: data,
    interpolate: d3.curveLinear,
    full_width: true,
    height: 300,
    target: '#event-registration',
    y_accessor: 'total',
    legend: ['Registration','Attendance'],
    legend_target: '#events-legend',
    aggregate_rollover: true
  })
})
