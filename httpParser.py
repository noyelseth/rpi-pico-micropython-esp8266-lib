
class HttpParser:
    """
    This is a class for parse HTTP response, coming from ESP8266 after complete the Post/Get operation
    Using this class, you parse the HTTP Post/Get operation's response and get HTTP status code, Response.
    """
    
    __httpErrorCode=None
    __httpHeader=None
    __httpResponseLength=None
    __httpResponse=None
    
    def __init__(self):
        """
        The constaructor for HttpParser class
        """
        self.__httpErrCode=None
        self.__httpHeader=None
        self.__httpResponseLength=None
        self.__httpResponse=None
        
    def parseHTTP(self, httpRes):
        """
        This funtion use to parse the HTTP response and return back the HTTP status code
        
        Return:
            HTTP status code.
        """
        if httpRes is not None:
            self.__httpResponse = httpRes.split(b'\r\n\r\n')[3]

            header = str(httpRes.split(b'\r\n\r\n')[2], 'utf-8')
            self.__httpHeader = header[header.index('HTTP'):]

            for code in str(self.__httpHeader.partition(r"\r\n")[0]).split():
                if code.isdigit():
                    self.__httpErrCode = int(code)
                    break

            if self.__httpErrCode != 200:
                self.__httpResponse = None

            return self.__httpErrCode
        else:
            return 0
    
    def getHTTPErrCode(self):
        """
        This funtion use to get latest parsed HTTP response's status code
        
        Return:
            HTTP status code.
        """
        return self.__httpErrCode
    
    def getHTTPResponse(self):
        """
        This funtion use to get latest parsed HTTP response's response massage.
        
        Return:
            HTTP response message.
        """
        return self.__httpResponse
    
    def __del__(self):
        """
        The distaructor for HttpParser class
        """
        pass
    
