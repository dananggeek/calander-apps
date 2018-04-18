function deleteCalender(entry){
  var $entry = $(entry)
  $$entry.parent().remove()
  var id = $entry.data('id')

  $.ajax({
    url: 'entry/delete/' + id,
    method : 'POST',
    data : {
      'csrfmiddlewaretoken':csrf_tokenf
    },
  })
}
