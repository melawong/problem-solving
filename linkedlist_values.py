def linked_list_values(head):
  values = []
  current = head

  while current is not None:
    values.append(current.val)
    current = current.next

  return values