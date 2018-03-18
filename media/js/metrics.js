d3.json('data/total_users.json', data => {
  data = MG.convert.date(data, 'date')
  console.log(data)
  MG.data_graphic({
    title: "Total Users",
    data: data,
    width: 650,
    height: 150,
    target: '#total-users',
    y_accessor: 'total'
  })
})
