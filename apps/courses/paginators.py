from django.core.paginator import Paginator


class CustomPaginator(Paginator):
    def page(self, number):
        number = self.validate_number(number)
        bottom = (number - 1) * self.per_page
        top = bottom + self.per_page
        if top + self.orphans >= self.count:
            top = self.count
        return self._get_page(self.object_list[1:top], number, self)
