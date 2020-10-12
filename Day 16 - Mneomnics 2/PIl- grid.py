from PIL import Image
import numpy as np

def pil_grid(images, max_horiz=np.iinfo(int).max):
    n_images = len(images)
    n_horiz = min(n_images, max_horiz)
    h_sizes, v_sizes = [0] * n_horiz, [0] * (n_images // n_horiz)
    for i, im in enumerate(images):
        h, v = i % n_horiz, i // n_horiz
        h_sizes[h] = max(h_sizes[h], im.size[0])
        v_sizes[v] = max(v_sizes[v], im.size[1])
    h_sizes, v_sizes = np.cumsum([0] + h_sizes), np.cumsum([0] + v_sizes)
    im_grid = Image.new('RGB', (h_sizes[-1], v_sizes[-1]), color='white')
    for i, im in enumerate(images):
        im_grid.paste(im, (h_sizes[i % n_horiz], v_sizes[i // n_horiz]))
    return im_grid

def dummy(w, h):
    "Produces a dummy PIL image of given dimensions"
    from PIL import ImageDraw
    im = Image.new('RGB', (w, h), color=tuple((np.random.rand(3) * 255).astype(np.uint8)))
    draw = ImageDraw.Draw(im)
    points = [(i, j) for i in (0, im.size[0]) for j in (0, im.size[1])]
    for i in range(len(points) - 1):
        for j in range(i+1, len(points)):
            draw.line(points[i] + points[j], fill='black', width=2)
    return im

dummy_images = [dummy(20 + np.random.randint(30), 20 + np.random.randint(30)) for _ in range(10)]

dummy_images.save("dummy_images.jpg")