#include <igtlMessageFactory.h>
#include <igtlMessageHeader.h>
#include <igtlTransformMessage.h>

#include <stdexcept>

#define EXIT_SUCCESS 0
#define EXIT_FAILURE 1

int main() {

    igtl::MessageFactory::Pointer factory = igtl::MessageFactory::New();

    igtl::MessageHeader::Pointer header = NULL;

    if (factory->IsValid(header))
    {
        std::cerr << "A null header is not valid." << std::endl;
        return EXIT_FAILURE;
    }

    header = igtl::MessageHeader::New();

    if (factory->IsValid(header))
    {
        std::cerr << "A header without a DeviceType e.g. STRING, TRANSFORM is invalid." << std::endl;
        return EXIT_FAILURE;
    }

    igtl::TransformMessage::Pointer transformMessage = igtl::TransformMessage::New();

    if (!factory->IsValid(transformMessage.GetPointer()))
    {
        std::cerr << "The IsValid method should check for not null, and a valid DeviceType. TRANSFORM should be valid." << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}