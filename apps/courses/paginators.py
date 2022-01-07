from django.core.paginator import Paginator


class CustomPaginator(Paginator):
    per_page = 10

    def page(self, number):
        number = self.validate_number(number)
        bottom = (number - 1) * self.per_page
        top = bottom + self.per_page
        return self._get_page(self.object_list[0:top], number, self)
