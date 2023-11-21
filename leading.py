from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
import pprint

def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def get_image(image_path):
    image_path = image_path.replace("\\", "/")
    print(image_path)
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.axis('off')
    plt.imshow(image)
    plt.title("Inserted image : " + image_path.split("/")[-1])
    plt.show()
    return image

def color_extractor(image, number_of_colors, new_shape=(3, 3), plot_pie=True, plot_cls_c=True, plot_highest_ratio=True, top_n=[5, 10]):
    modified_image_1 = cv2.resize(image, new_shape, interpolation=cv2.INTER_AREA)
    modified_image = modified_image_1.reshape(modified_image_1.shape[0] * modified_image_1.shape[1], 3)

    clf = KMeans(n_clusters=number_of_colors)
    labels = clf.fit_predict(modified_image)

    counts = Counter(labels)
    center_colors = clf.cluster_centers_
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]

    # Sort colors based on frequency
    sorted_colors = sorted(zip(hex_colors, counts.values()), key=lambda x: x[1], reverse=True)

    for n in top_n:
        # Extract top colors and their counts
        top_hex_colors, top_counts = zip(*sorted_colors[:n])

        result = {
            "number_of_colors": number_of_colors,
            "color_values": [val for val in counts.values()],
            "rgb_colors": rgb_colors,
            "hex colors": hex_colors,
            "dominant_color": {"index": 0, "color_in_rgb": rgb_colors[0], "color_in_hex": hex_colors[0]},
            f"top_{n}_colors": {"hex_colors": top_hex_colors, "counts": top_counts}
        }

        if plot_highest_ratio:
            plt.figure(figsize=(6, 4))
            plt.title(f"Top {n} Colors")
            plt.bar(top_hex_colors, top_counts, color=top_hex_colors)
            plt.xlabel("Color")
            plt.ylabel("Count")
            plt.show()

        pprint.pprint(result)

path = r"Image Hex Code/claudio-schwarz-jSqwyZ5gP0U-unsplash.jpg"

image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(image)
print("The type of this input is {}".format(type(image)))
print("Shape: {}".format(image.shape))
plt.axis('off')
plt.imshow(image)

color_extractor(get_image(path), 10, (100, 80), plot_pie=False, plot_cls_c=False, plot_highest_ratio=True, top_n=[5, 10])
