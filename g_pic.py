from PIL import Image, ImageDraw, ImageOps
import os


def remove_background(image, background_color=(255, 255, 255)):
    # Создаем маску на основе цвета фона
    mask = Image.new("L", image.size, 0)
    pixels = image.load()
    mask_pixels = mask.load()
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            if pixels[x, y][:3] != background_color:
                mask_pixels[x, y] = 255
    image.putalpha(mask)
    return image


def generate_images(input_path, output_folder, num_images=10, final_width=1220, final_height=800):
    # Открываем исходное изображение и убираем белый фон
    base_image = Image.open(input_path).convert("RGBA")
    base_image = remove_background(base_image)

    # Извлекаем имя файла без расширения и пути
    base_name = os.path.splitext(os.path.basename(input_path))[0]

    # Создаем папку для сохранения изображений, если она не существует
    os.makedirs(output_folder, exist_ok=True)

    for i in range(1, num_images + 1):
        # Определяем количество объектов на текущем изображении
        num_objects = i

        # Определяем количество объектов в строке и столбце
        objects_per_row = min(num_objects, 5)
        num_rows = (num_objects + 4) // 5  # 1-5 objects -> 1 row, 6-10 objects -> 2 rows
        object_size = min(final_width // objects_per_row, final_height // num_rows)

        # Создаем белый фон для изображения
        image = Image.new('RGBA', (final_width, final_height), (255, 255, 255, 255))

        # Вычисляем начало вставки для центрирования по вертикали
        total_height = num_rows * object_size
        start_y = (final_height - total_height) // 2

        # Вставляем элементы на изображение
        for j in range(num_objects):
            # Определяем позицию вставки
            row = j // 5
            col = j % 5
            total_width = objects_per_row * object_size
            start_x = (final_width - total_width) // 2

            x = start_x + col * object_size
            y = start_y + row * object_size

            # Изменяем размер элемента
            resized_base_image = base_image.resize((object_size, object_size), Image.LANCZOS)

            # Вставляем элемент
            image.paste(resized_base_image, (x, y), resized_base_image)

        # Формируем имя для нового изображения
        new_image_name = f"{base_name}{i}.png"
        new_image_path = os.path.join(output_folder, new_image_name)

        # Сохраняем новое изображение
        image.save(new_image_path)

        print(f"Saved: {new_image_path}")


# Пример использования функции
generate_images('static/pic_trainer/snow.png', 'static/pic_trainer', num_images=10, final_width=1220, final_height=800)
