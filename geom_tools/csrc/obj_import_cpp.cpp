#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <optional>
#include <vector>
#include <string>
#include <sstream>
#include <stdint.h>
#include <iostream>


const char spaceDelim = ' ';


inline bool iterateStreamUntilNonEmpty(
    std::istringstream &lineStream,
    std::string &tokenBuffer)
{
    bool isStoppedByGoodToken = false;
    while (std::getline(lineStream, tokenBuffer, spaceDelim)) {
        if (tokenBuffer.size() > 0) {
            isStoppedByGoodToken = true;
            break;
        }
    }
    return isStoppedByGoodToken;
}


std::optional<float> tryStrToFloat(const std::string &string)
{
    std::optional<float> res;
    try {
        res = std::stof(string);
    } catch (...) {
        res = {};
    }
    return res;
}


inline bool readVertex3DToFlatArray(
    std::istringstream &lineStream,
    std::string &token,
    std::vector<float> &vertices)
{
    const int nTokensInVertex = 3;
    for (int i = 0; i < nTokensInVertex; ++i) {
        const bool isTokenReadingOk = iterateStreamUntilNonEmpty(lineStream, token);
        if (!isTokenReadingOk)
            return false;
        const std::optional<float> parseRes = tryStrToFloat(token);
        if (parseRes.has_value())
            vertices.push_back(parseRes.value());
        else
            return false;
    }
    return true;
}


std::optional<std::vector<float>> readFlatVerticesFromString(const std::string &allLines)
{
    std::stringstream linesStream(allLines);

    std::vector<float> verticesFlat;

    std::string tokenBuffer;

    for (std::string line; std::getline(linesStream, line); ) {
        std::istringstream lineStream(line);

        iterateStreamUntilNonEmpty(lineStream, tokenBuffer);

        if (tokenBuffer.size() < 1)
            continue;

        if ((tokenBuffer[0] == 'v') && (tokenBuffer.size() == 1)) {
            const bool isOk = readVertex3DToFlatArray(lineStream, tokenBuffer, verticesFlat);
            if (!isOk)
                return {};
        }
    }

    return verticesFlat;
}


PYBIND11_MODULE(obj_import_cpp, m) {
    m.def("read_flat_vertices_from_string", &readFlatVerticesFromString, "");
}
