use image::GenericImageView;
use image::imageops;
use image::GenericImage;
use image::ColorType;

fn main() {
    let mut img = image::open("test.jpg").unwrap();
    let mut n = img.resize(800,1000000, imageops::FilterType::Gaussian);
    let mut a = n.into_luma8();

    imageops::dither(&mut a, &image::imageops::colorops::BiLevel);
    a.save("test_dither.png").unwrap();
}
