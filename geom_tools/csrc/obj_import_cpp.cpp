#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <string>
#include <sstream>
#include <stdint.h>
#include <iostream>


const char spaceDelim = ' ';


inline void iterateStreamUntilNonEmpty(
    std::istringstream &lineStream,
    std::string &tokenBuffer)
{
    while (std::getline(lineStream, tokenBuffer, spaceDelim))
        if (tokenBuffer.size() > 0)
            break;
}


inline void readVertex3D(
    std::istringstream &lineStream,
    std::string &token,
    std::vector<float> &vertices)
{
    iterateStreamUntilNonEmpty(lineStream, token);
    vertices.push_back(std::stof(token));
    iterateStreamUntilNonEmpty(lineStream, token);
    vertices.push_back(std::stof(token));
    iterateStreamUntilNonEmpty(lineStream, token);
    vertices.push_back(std::stof(token));
}


std::vector<float> readFlatVerticesFromString(const std::string &allLines)
{
    std::stringstream linesStream(allLines);

    std::vector<float> vertices;

    std::string tokenBuffer;

    for (std::string line; std::getline(linesStream, line); ) {
        std::istringstream lineStream(line);

        iterateStreamUntilNonEmpty(lineStream, tokenBuffer);

        if (tokenBuffer.size() < 1)
            continue;

        if ((tokenBuffer[0] == 'v') && (tokenBuffer.size() == 1))
            readVertex3D(lineStream, tokenBuffer, vertices);
    }

    return vertices;
}


PYBIND11_MODULE(obj_import_cpp, m) {
    m.def("read_flat_vertices_from_string", &readFlatVerticesFromString, "");
}
