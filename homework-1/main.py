from src.item import Item
from src.channel import Channel

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    print(item1.calculate_total_price())  # 200000
    print(item2.calculate_total_price())  # 100000

    # устанавливаем новый уровень цен
    Item.pay_rate = 0.8
    # применяем скидку
    item1.apply_discount()

    print(item1.price)  # 8000.0
    print(item2.price)  # 20000

    print(Item.all)  # [<__main__.Item object at 0x000001EC6250C690>, <__main__.Item object at 0x000001EC6250C6D0>]


if __name__ == '__main__':
    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    print(vdud.print_info())

    """
{
  "kind": "youtube#channelListResponse",
  "etag": "TUX2o600Qs42JSCO9hckmDv7scY",
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 5
  },
  "items": [
    {
      "kind": "youtube#channel",
      "etag": "SsK2QuB-f3WnRrph7tt5yppfuN8",
      "id": "UCMCgOm8GZkHp8zJ6l7_hIuA",
      "snippet": {
        "title": "вДудь",
        "description": "Здесь задают вопросы",
        "customUrl": "@vdud",
        "publishedAt": "2014-01-03T06:27:22Z",
        "thumbnails": {
          "default": {
            "url": "https://yt3.ggpht.com/ytc/AL5GRJV2Av2ouJAjcHnaA8jokTI4uq6DZLnfHJm6T8vw=s88-c-k-c0x00ffffff-no-rj",
            "width": 88,
            "height": 88
          },
          "medium": {
            "url": "https://yt3.ggpht.com/ytc/AL5GRJV2Av2ouJAjcHnaA8jokTI4uq6DZLnfHJm6T8vw=s240-c-k-c0x00ffffff-no-rj",
            "width": 240,
            "height": 240
          },
          "high": {
            "url": "https://yt3.ggpht.com/ytc/AL5GRJV2Av2ouJAjcHnaA8jokTI4uq6DZLnfHJm6T8vw=s800-c-k-c0x00ffffff-no-rj",
            "width": 800,
            "height": 800
          }
        },
        "localized": {
          "title": "вДудь",
          "description": "Здесь задают вопросы"
        }
      },
      "statistics": {
        "viewCount": "1925259492",
        "subscriberCount": "10300000",
        "hiddenSubscriberCount": false,
        "videoCount": "163"
      }
    }
  ]
}
    """
